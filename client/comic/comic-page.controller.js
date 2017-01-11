
function ComicPageController(comicAPIService, $stateParams) {
    const ctrl = this;
    ctrl.issueId = $stateParams.issueId;

    function getComics() {
        const issueId = { id: $stateParams.issueId };
        return comicAPIService.issue.get(issueId).$promise.then((data) => {
            ctrl.comics = data.comic_set;
            console.log('data: ', data);
        });
    }

    // function getAllComics() {
    //     return comicAPIService.comic.get().$promise.then((data) => {
    //         ctrl.comics = data.results;
    //     });
    // }

    function init() {
        getComics();
    }

    init();
}

export default ComicPageController;

