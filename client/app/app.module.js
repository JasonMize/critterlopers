import angular from 'angular';

import appComponent from './app.component';

import ComicModule from '../comic/comic.module';

const AppModule = angular.module('app', [
    ComicModule.name,
])
    .component('app', appComponent);

export default AppModule;

