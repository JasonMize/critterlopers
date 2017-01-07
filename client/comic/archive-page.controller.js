
function ArchivePageController(comicAPIService) {
    const ctrl = this;


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

export default ArchivePageController;

