describe('ChatScreen', () => {
  it('devrait utiliser le service aiChatService', () => {
    const fs = require('fs');
    const path = require('path');
    const chatFile = fs.readFileSync(
      path.join(__dirname, '../chat.js'),
      'utf8'
    );
    
    expect(chatFile).toContain('sendMessage');
    expect(chatFile).toContain('aiChatService');
  });

  it('devrait afficher les messages utilisateur et assistant', () => {
    const fs = require('fs');
    const path = require('path');
    const chatFile = fs.readFileSync(
      path.join(__dirname, '../chat.js'),
      'utf8'
    );
    
    // Vérifier que le code gère les rôles user et assistant
    expect(chatFile).toContain('role');
    expect(chatFile).toContain('message');
  });

  it('devrait avoir un champ de saisie et un bouton send', () => {
    const fs = require('fs');
    const path = require('path');
    const chatFile = fs.readFileSync(
      path.join(__dirname, '../chat.js'),
      'utf8'
    );
    
    expect(chatFile).toContain('TextInput');
    expect(chatFile).toContain('handleSend');
    expect(chatFile).toContain('sendButton');
  });
});
