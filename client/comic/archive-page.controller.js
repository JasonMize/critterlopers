
function ArchivePageController(comicAPIService) {
    const archCtrl = this;

    function getAllComics() {
        // console.log('GET ALL COMICS CALLED');
        return comicAPIService.comic.get().$promise.then((data) => {
            archCtrl.comics = data.results;
            console.log('ALL COMICS ARCHIVE: ', archCtrl.comics);
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

