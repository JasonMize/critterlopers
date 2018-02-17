
function ComicPageController(comicAPIService, $stateParams) {
    console.log('COMIC PAGE CONTROLLER: $stateParams: ', $stateParams);
    const ctrl = this;

    function getComic() {
        return comicAPIService.getComic(
            $stateParams.pageNumber
        )
        .then((data) => {
            ctrl.comic = data;
            console.log('COMIC: ', ctrl.comic);
        });
    }

    function init() {
        getComic();
    }

    init();
}

export default ComicPageController;

