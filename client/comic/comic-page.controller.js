
function ComicPageController(comicAPIService, $stateParams) {
    const ctrl = this;
    ctrl.issueId = $stateParams.issueId;
    ctrl.comicId = $stateParams.comicId;



    function getComics() {
        const issueId = { id: $stateParams.issueId };
        return comicAPIService.issue.get(issueId).$promise.then((data) => {
            ctrl.comics = data.comic_set;
            console.log('data: ', data);
            console.log('comics: ', ctrl.comics);
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

