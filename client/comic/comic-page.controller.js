
function ComicPageController(comicAPIService, $stateParams) {
    const ctrl = this;

    function getComic() {
        return comicAPIService.getComic(
            $stateParams.issueId,
            $stateParams.pageNumber,
            $stateParams.navigation
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

