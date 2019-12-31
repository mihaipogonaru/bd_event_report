// place any jQuery/helper plugins in here, instead of separate, slower script files.
function show_snackbar(message) {
    'use strict';
    var data = {
      message: message,
      timeout: 2000
    };
    document.addEventListener('mdl-componentupgraded', function(e) {
        if (typeof e.target.MaterialSnackbar !== 'undefined') {
            e.target.MaterialSnackbar.showSnackbar(data);
        }
    });
};
