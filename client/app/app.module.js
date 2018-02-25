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

        // removes'#' from url path
        $locationProvider.html5Mode(true);

        // handles error from angular-ui-router and angularjs updates not working together
        function handleError ($qProvider){
            $qProvider.errorOnUnhandledRejections(false);
        };
        handleError($qProvider);

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

        // Google Analytics
        window.ga('create', 'UA-114427488-1', 'auto'); 
    });




export default AppModule;

