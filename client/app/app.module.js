import angular from 'angular';
import uiRouter from 'angular-ui-router';
import angularCookies from 'angular-cookies';
import timer from 'angular-timer';

import ComicModule from '../comic/comic.module';
import appComponent from './app.component';


const AppModule = angular.module('app', [
    uiRouter,
    angularCookies,
    ComicModule.name,
])
    .component('app', appComponent)

    .config(($stateProvider, $urlRouterProvider) => {
        $urlRouterProvider.otherwise('/');

        $stateProvider
            .state('index', {
                url: '/',
                component: 'comicPage',
            })

            .state('aboutPage', {
                url: '/about',
                component: 'aboutPage',
            });
    })

    .run(($http, $cookies) => {
        // Add a header for CSRF token, so that POST does not fail to our API
        // eslint-disable-next-line no-param-reassign
        $http.defaults.headers.common['X-CSRFToken'] = $cookies.get('csrftoken');
    });

export default AppModule;

