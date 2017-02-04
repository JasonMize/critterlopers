
function ArchivePageController(comicAPIService) {
    const ctrl = this;


    function getAllComics() {
        console.log('GET ALL COMICS CALLED');
        return comicAPIService.comic.get().$promise.then((data) => {
            ctrl.comics = data.results;
            console.log('ALL COMICS ARCHIVE: ', ctrl.comics);
        }, (error) => {
            console.log('ERROR: ', error);
        });
    }

    function init() {
        getAllComics();
    }

    init();
}

export default ArchivePageController;

