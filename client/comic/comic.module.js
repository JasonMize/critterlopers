import angular from 'angular';
import angularResource from 'angular-resource';

import comicAPIService from './comic-api.service';
import comicPageComponent from './comic-page.component';
import aboutPageComponent from './about-page.component';

const ComicModule = angular.module('comics', [
    angularResource,
])
    .config(($resourceProvider) => {
        // eslint-disable-next-line no-param-reassign
        $resourceProvider.defaults.stripTrailingSlashes = false;
    })
    .factory('comicAPIService', comicAPIService)
    .component('comicPage', comicPageComponent)
    .component('aboutPage', aboutPageComponent);

export default ComicModule;
