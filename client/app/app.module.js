import angular from 'angular';
import uiRouter from 'angular-ui-router';
import angularCookies from 'angular-cookies';

import ComicModule from '../comic/comic.module';
import appComponent from './app.component';


const AppModule = angular.module('app', [
    uiRouter,
    angularCookies,
    ComicModule.name,
])
    .component('app', appComponent)

    .config(($stateProvider, $urlRouterProvider, $locationProvider, $qProvider) => {
        $urlRouterProvider.otherwise('/');
        $locationProvider.html5Mode(true);

        function $qProvider ($qProvider){
            $qProvider.errorOnUnhandledRejections(false);
        };

        $stateProvider
        .state('aboutPage', {
            url: '/about',
            component: 'aboutPage',
        })

        .state('archivePage', {
            url: '/archive',
            component: 'archivePage',
        })

        .state('castPage', {
            url: '/cast',
            component: 'castPage',
        })

        .state('index', {
            url: '/comic/{pageNumber: [0-9]+}',
            component: 'comicPage',
            resolve: {
                comic(comicAPIService, $stateParams) {
                    return comicAPIService
                    .getComic(
                        $stateParams.pageNumber,
                    );
                },
            },
        });
    })

    .run(($http, $cookies, $stateParams) => {
        console.log('HTTP: ', $stateParams);

        // Add a header for CSRF token, so that POST does not fail to our API
        // eslint-disable-next-line no-param-reassign
        $http.defaults.headers.common['X-CSRFToken'] = $cookies.get('csrftoken');
        let page;
        // send updated of page changes to Google Analytics
        // $rootScope.$on('$stateChangeSuccess', function (event) {
        if ($stateParams.pageNumber != page) {
            page = $stateParams.pageNumber;
            ga('send', 'pageview');
        }
    });




export default AppModule;

