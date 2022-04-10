function reloadUrls(){
    $('.urls-box').empty();
    $.ajax("/", {
        type: 'GET',
        statusCode: {
            200: (data) => {
                console.log(data);
                $('.urls-box').empty();
                if (Object.entries(data).length < 1){
                    $('.urls-box').append(`
                        You have not shorten any URL
                    `);
                    return;
                }
                $('.urls-box').append(`
                    <h4> Your Urls: </h4>
                    ${Object.entries(data).map((e) => {
                        const shortened = e[0];
                        const original = e[1]
                        return `
                            <div class="url-container">
                                <a class="my_url" target="_blank" href="${`/${shortened}`}">
                                    ${shortened}
                                </a>
                                <div class="original-url">
                                    ${original}
                                </div>
                                <div class="delete-url" style="cursor: pointer">
                                    <span id="delete-${shortened}" class="material-icons" style="color: #bc0031">close</span>
                                </div>
                            </div>
                        `;
                    }).join(' ')}
                `);
                $('.delete-url').click((ev) => {
                    const urlId = $(this).children('span').attr('id');
                    console.log($(this).children('span'));
                    console.log(urlId);
                    $.ajax(`/${urlId.split('-')[1]}`, {
                        type: 'DELETE',
                        statusCode: {
                            204: (res) => {
                                reloadUrls();
                            },
                            404: () => {
                                reloadUrls();
                            },
                            500: () => {
                                $('#extra-message').append(`
                                   'Unknown error'
                                `);
                            }
                        }
                    });
                });
            },
            500: (err) => {
                console.log(err);
                $('.url-container').append(`
                    An error has occurred
                `)
            }
        }
    });
}

$(document).ready(function(){

    reloadUrls();

    $('#create-url').click(() => {
        let newUrl = $('#new-url').val();
        $('#extra-message').empty();
        $.ajax('/', {
            type: 'POST',
            data: { url: newUrl },
            statusCode: {
                201: (res) => {
                    $('#new-url').val('');
                    $('#extra-message').empty();
                    reloadUrls();
                },
                401: () => {
                    $('#extra-message').append(`
                       URL format is not correct
                    `);
                },
                500: () => {
                    $('#extra-message').append(`
                       'Unknown error'
                    `);
                }
            }
        });
    });

    $('#deleteAll').click(() => {
        $.ajax('/', {
            type: 'DELETE',
            statusCode: {
                200: (res) => {
                    reloadUrls();
                },
                404: () => {
                    reloadUrls();
                },
                500: () => {
                    $('#extra-message').append(`
                       'Unknown error'
                    `);
                }
            }
        });
        reloadUrls();
    });
});