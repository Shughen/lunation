#!/usr/bin/env node
/**
 * MCP Server - Astroia Lunar
 *
 * Serveur MCP minimaliste qui permet d'exécuter UNIQUEMENT les scripts tools/*.sh
 * Rejette toute autre commande pour des raisons de sécurité.
 */

const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');

// Scripts autorisés (allowlist stricte)
const ALLOWED_SCRIPTS = [
  'tools/build_android.sh',
  'tools/run_tests_mobile.sh',
  'tools/run_tests_api.sh',
  'tools/collect_logcat.sh',
  'tools/start_expo.sh'
];

// Racine du repo (1 niveau au-dessus de tools/)
const REPO_ROOT = path.join(__dirname, '..');

/**
 * Vérifie si un script est autorisé
 */
function isAllowed(command) {
  return ALLOWED_SCRIPTS.includes(command);
}

/**
 * Exécute un script autorisé
 */
function executeScript(scriptPath) {
  return new Promise((resolve, reject) => {
    const fullPath = path.join(REPO_ROOT, scriptPath);

    // Vérifier que le script existe
    if (!fs.existsSync(fullPath)) {
      reject(new Error(`Script not found: ${scriptPath}`));
      return;
    }

    // Vérifier que le script est exécutable
    try {
      fs.accessSync(fullPath, fs.constants.X_OK);
    } catch (err) {
      reject(new Error(`Script not executable: ${scriptPath}`));
      return;
    }

    // Exécuter le script
    const proc = spawn(fullPath, [], {
      cwd: REPO_ROOT,
      stdio: 'pipe',
      shell: false
    });

    let stdout = '';
    let stderr = '';

    proc.stdout.on('data', (data) => {
      stdout += data.toString();
    });

    proc.stderr.on('data', (data) => {
      stderr += data.toString();
    });

    proc.on('close', (code) => {
      resolve({
        exitCode: code,
        stdout,
        stderr
      });
    });

    proc.on('error', (err) => {
      reject(err);
    });
  });
}

/**
 * Handler MCP : execute_command
 */
async function handleExecuteCommand(params) {
  const { command } = params;

  // Vérifier que la commande est autorisée
  if (!isAllowed(command)) {
    return {
      error: `Command not allowed: ${command}\n\nAllowed scripts:\n${ALLOWED_SCRIPTS.map(s => `  - ${s}`).join('\n')}`
    };
  }

  try {
    const result = await executeScript(command);

    // Formater la sortie
    let output = '';
    if (result.stdout) {
      output += result.stdout;
    }
    if (result.stderr) {
      output += '\n--- STDERR ---\n' + result.stderr;
    }
    output += `\n--- EXIT CODE: ${result.exitCode} ---`;

    return {
      output,
      exitCode: result.exitCode
    };
  } catch (err) {
    return {
      error: `Execution failed: ${err.message}`
    };
  }
}

/**
 * MCP Protocol Handler
 */
async function handleMCPRequest(request) {
  const { method, params } = request;

  switch (method) {
    case 'tools/list':
      return {
        tools: [
          {
            name: 'execute_command',
            description: 'Execute an allowed script from tools/ directory',
            inputSchema: {
              type: 'object',
              properties: {
                command: {
                  type: 'string',
                  description: 'Script path (e.g., tools/build_android.sh)',
                  enum: ALLOWED_SCRIPTS
                }
              },
              required: ['command']
            }
          }
        ]
      };

    case 'tools/call':
      if (params.name === 'execute_command') {
        return await handleExecuteCommand(params.arguments);
      }
      return { error: 'Unknown tool' };

    default:
      return { error: 'Unknown method' };
  }
}

/**
 * Main: Lire stdin (JSON-RPC), répondre sur stdout
 */
async function main() {
  let buffer = '';

  process.stdin.setEncoding('utf8');

  process.stdin.on('data', async (chunk) => {
    buffer += chunk;

    // Essayer de parser chaque ligne JSON
    const lines = buffer.split('\n');
    buffer = lines.pop(); // Garder la dernière ligne incomplète

    for (const line of lines) {
      if (!line.trim()) continue;

      try {
        const request = JSON.parse(line);
        const response = await handleMCPRequest(request);

        // Répondre avec le même ID
        const result = {
          jsonrpc: '2.0',
          id: request.id,
          result: response
        };

        process.stdout.write(JSON.stringify(result) + '\n');
      } catch (err) {
        console.error('Error processing request:', err);
      }
    }
  });

  process.stdin.on('end', () => {
    process.exit(0);
  });
}

// Lancer le serveur
main();
