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

    .config(($stateProvider, $urlRouterProvider, $locationProvider) => {
        $urlRouterProvider.otherwise('/');
        $locationProvider.html5Mode(true);
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
                        $stateParams.pageNumber
                    );
                },
            },
        });
    })

    .run(($http, $cookies) => {
        // Add a header for CSRF token, so that POST does not fail to our API
        // eslint-disable-next-line no-param-reassign
        $http.defaults.headers.common['X-CSRFToken'] = $cookies.get('csrftoken');
    });

export default AppModule;

