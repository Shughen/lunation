/**
 * Helpers pour mocker Supabase dans les tests
 * 
 * Ce module fournit des utilitaires réutilisables pour créer des mocks Supabase
 * cohérents dans tous les tests.
 */

/**
 * Crée un mock de query builder Supabase
 * 
 * @param {Object} response - La réponse à retourner par la query
 * @param {Object} response.data - Les données retournées
 * @param {Object} response.error - L'erreur éventuelle
 * @returns {Object} Un objet mock qui implémente la chaîne de méthodes Supabase
 * 
 * @example
 * const query = createQueryMock({ data: { id: 1 }, error: null });
 * supabase.from.mockReturnValue(query);
 */
export function createQueryMock(response) {
  const query = {
    insert: jest.fn(() => query),
    select: jest.fn(() => query),
    eq: jest.fn(() => query),
    order: jest.fn(() => query),
    limit: jest.fn(() => query),
    single: jest.fn(() => Promise.resolve(response)),
    maybeSingle: jest.fn(() => Promise.resolve(response)),
    // Pour les queries qui retournent un array
    then: (resolve) => Promise.resolve(response).then(resolve),
  };

  return query;
}

/**
 * Crée un mock de client Supabase basique
 * 
 * @returns {Object} Un mock de client Supabase avec les méthodes communes
 */
export function createSupabaseClientMock() {
  return {
    auth: {
      getUser: jest.fn(),
      signInWithPassword: jest.fn(),
      signOut: jest.fn(),
    },
    from: jest.fn(),
    rpc: jest.fn(),
  };
}

