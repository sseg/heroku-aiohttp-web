// See http://brunch.io/#documentation for docs.

module.exports = {
  paths: {
    public: 'public',
    watched: ['assets']
  },

  files: {
    javascripts: {joinTo: 'js/app.js'},
    stylesheets: {joinTo: 'css/app.css'}   
  },

  conventions: {
    assets: /assets\/digest[\\/]/
  },

  plugins: {
    digest: {manifest: 'manifest.json', alwaysRun: true}
  },

  hooks: {
    onCompile: (generatedFiles, changedAssets) => {
      console.log(generatedFiles.map(f => f.path));
    }
  }
};

