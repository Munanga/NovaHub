var $spinner = $('#spinner').hide();
var $cancelButton = $('#cancel-box').hide();

const uploadForm = document.getElementById('upload-form')
const input = document.getElementById('id_uploaded_file')
console.log(input)

const alertBox = document.getElementById('alert-box')
const imageBox = document.getElementById('image-box')
const progressBox = document.getElementById('progress-box')
const cancelBox = document.getElementById('cancel-box')
const cancelBtn = document.getElementById('cancel-btn')

const csrf = document.getElementsByName('csrfmiddlewaretoken')

input.addEventListener('change', ()=>{
    progressBox.classList.remove('not-visible')
    cancelBox.classList.remove('not-visible')

    const file_data = input.files[0]
    const url = URL.createObjectURL(file_data)

    const fd = new FormData()
    fd.append('csrfmiddlewaretoken', csrf[0].value)
    fd.append('uploaded_file', file_data)

    $.ajax({
        type:'POST',
        url: uploadForm.action,
        enctype: 'multipart/form-data',
        data: fd,
        beforeSend: function(){
            console.log('before')
            alertBox.innerHTML= ""
            imageBox.innerHTML = ""
        },


        xhr: function(){
            const xhr = new window.XMLHttpRequest();

            xhr.upload.addEventListener('progress', e=>{

                if (e.lengthComputable) {
                    percent = e.loaded / e.total;
                    percent = percent * 100;
                    $spinner.show();
                    $cancelButton.show();
                    alertBox.innerHTML = `<div class="alert alert-primary" role="alert">
                                    Uploading your file please wait.😊
                                </div>`
                }
            })


            cancelBtn.addEventListener('click', ()=>{
                xhr.abort()
                setTimeout(()=>{
                    uploadForm.reset()
                    progressBox.innerHTML=""
                    alertBox.innerHTML = `<div class="alert alert-danger" role="alert">
                                    File upload canceled.
                                </div>`
                    cancelBox.classList.add('not-visible')
                }, 2000)
            })
            return xhr;
        },



        success: function(response){
            $spinner.hide();
            $cancelButton.hide();
            alertBox.innerHTML = `<div class="alert alert-success" role="alert">
                                    Successfully uploaded your file
                                </div>`
            cancelBox.classList.add('not-visible')
            window.location.href = "/"
        },

        error: function(error){
            $spinner.hide();
            $cancelButton.hide();
            console.log(error)
            alertBox.innerHTML = `<div class="alert alert-danger" role="alert">
                                    Oops... could not upload file.
                                </div>`
        },
        cache: false,
        contentType: false,
        processData: false,
    })


})

