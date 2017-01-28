
function ComicPageController(comicAPIService, $stateParams) {
    const ctrl = this;
    ctrl.issueId = $stateParams.issueId;
    ctrl.pageNumber = $stateParams.pageNumber;

    function getComic() {
        return comicAPIService.getComic($stateParams.issueId, $stateParams.pageNumber)
        .then((data) => {
            ctrl.comic = data;
            console.log('COMIC: ', ctrl.comic);
            // TODO: call get previous and call get next
        });
    }

    function init() {
        getComic();
    }

    init();
}

export default ComicPageController;

