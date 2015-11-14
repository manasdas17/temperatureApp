(function() {
    'use strict';

    function MainController($scope, $timeout, $http) {
        var vm = this;


        var response = $http({
            method: "GET",
            url: "http://localhost:5000/api"
        });

        response.success(function(data) {
            $scope.labels = [];
            $scope.series = ['Temperatura Interna', 'Temperatura Externa'];

            var tempInt = [],
                tempExt = [];

            angular.element.each(data.data, function() {
                $scope.labels.push(this.fecha);
                tempInt.push(parseInt(this.temps.int));
                tempExt.push(parseInt(this.temps.ext));
            });
            $scope.data = [tempInt, tempExt];
            $scope.tempInt = angular.element(tempInt).get(-1);
            $scope.tempExt = angular.element(tempExt).get(-1);

            $scope.colours = [
                '#F7464A', // red
                '#46BFBD', // green
            ];
        });

        $scope.onClick = function(points, evt) {
            console.log(points, evt);
        };

        function activate() {
            $timeout(function() {
                vm.classAnimation = 'rubberBand';
            }, 4000);
        }

        activate();

    }

    angular
        .module('ricveal')
        .controller('MainController', MainController);

})();
