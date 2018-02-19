import angular from 'angular';
import angularResource from 'angular-resource';

import comicAPIService from './comic-api.service';
import comicPageComponent from './comic-page.component';
import aboutPageComponent from './about-page.component';
import archivePageComponent from './archive-page.component';
// import castPageComponent from './cast-page.component';

const ComicModule = angular.module('comic', [
    angularResource,
])
    .config(($resourceProvider) => {
        // eslint-disable-next-line no-param-reassign
        $resourceProvider.defaults.stripTrailingSlashes = false;
    })
        .factory('comicAPIService', comicAPIService)
        .component('comicPage', comicPageComponent)
        .component('aboutPage', aboutPageComponent)
        .component('archivePage', archivePageComponent)
        // .component('castPage', castPageComponent)
    ;

export default ComicModule;
