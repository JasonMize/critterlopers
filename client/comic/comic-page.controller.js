
function ComicPageController(comicAPIService) {
    const ctrl = this;


    // function getCurrentComic() {
        
    // }

    function getAllComics() {
        return comicAPIService.comic.get().$promise.then((data) => {
            ctrl.comics = data.results;
        });
    }

    function init() {
        getAllComics();
    }

    init();
}

export default ComicPageController;

