(function() {
    'use strict';

    describe('controllers', function() {
        var vm;
        var $timeout;
        var toastr;

        beforeEach(module('ricveal'));
        beforeEach(inject(function(_$controller_, _$timeout_) {
            vm = _$controller_('MainController');
            $timeout = _$timeout_;
        }));
    });
})();
