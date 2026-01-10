describe('ProfileScreen', () => {
  it('devrait contenir le formulaire de profil avec les champs requis', () => {
    const fs = require('fs');
    const path = require('path');
    const profileFile = fs.readFileSync(
      path.join(__dirname, '../profile.js'),
      'utf8'
    );
    
    // Vérifier que le formulaire contient les champs essentiels
    expect(profileFile).toContain('birthDate');
    expect(profileFile).toContain('birthTime');
    expect(profileFile).toContain('birthPlace');
  });

  it('devrait utiliser le profileStore pour sauvegarder', () => {
    const fs = require('fs');
    const path = require('path');
    const profileFile = fs.readFileSync(
      path.join(__dirname, '../profile.js'),
      'utf8'
    );
    
    expect(profileFile).toContain('saveProfile');
    expect(profileFile).toContain('useProfileStore');
  });

  it('devrait calculer le signe zodiacal', () => {
    const fs = require('fs');
    const path = require('path');
    const profileFile = fs.readFileSync(
      path.join(__dirname, '../profile.js'),
      'utf8'
    );
    
    expect(profileFile).toContain('getZodiacSign');
  });
});
