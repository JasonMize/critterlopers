// import { range } from 'ramda';

function ComicPageController(comicAPIService) {
    const ctrl = this;


    // get a random HeaderImage
    function randomHeaderImage() {
        ctrl.maxRange = Math.floor(ctrl.headerImageList.length);
        ctrl.headerImageIndex = Math.floor(Math.random() * (ctrl.maxRange));
        ctrl.randomHeaderImage = ctrl.headerImageList[ctrl.headerImageIndex];
    }


    // get all HeaderImages
    function getHeaderImage() {
        return comicAPIService.headerimage.get().$promise.then((data) => {
            ctrl.headerImageList = data.results;

            randomHeaderImage();
        });
    }


    function init() {
        getHeaderImage();
    }

    init();
}

export default ComicPageController;

