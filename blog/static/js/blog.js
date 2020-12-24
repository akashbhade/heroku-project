

document.addEventListener("DOMContentLoaded", function (event) {
    console.log("This is blog.js");
    let sc = document.createElement('script')
    sc.setAttribute('src', 'https://cdn.tiny.cloud/1/crgi5v6wte5lpov5iebof876pz3u7ycwrzww1j8mwxwmed2a/tinymce/5/tinymce.min.js');

    document.head.appendChild(sc);
    sc.onload = () => {
        tinymce.init({
            selector: '#id_content',
            plugins: 'print preview powerpaste casechange importcss tinydrive searchreplace autolink autosave save directionality advcode visualblocks visualchars fullscreen image link media mediaembed template codesample table charmap hr pagebreak nonbreaking anchor toc insertdatetime advlist lists checklist wordcount tinymcespellchecker a11ychecker imagetools textpattern noneditable help formatpainter permanentpen pageembed charmap tinycomments mentions quickbars linkchecker emoticons advtable',
  tinydrive_token_provider: 'URL_TO_YOUR_TOKEN_PROVIDER',
  tinydrive_dropbox_app_key: 'YOUR_DROPBOX_APP_KEY',
  tinydrive_google_drive_key: 'YOUR_GOOGLE_DRIVE_KEY',
  tinydrive_google_drive_client_id: 'YOUR_GOOGLE_DRIVE_CLIENT_ID',
  mobile: {
    plugins: 'print preview powerpaste casechange importcss tinydrive searchreplace autolink autosave save directionality advcode visualblocks visualchars fullscreen image link media mediaembed template codesample table charmap hr pagebreak nonbreaking anchor toc insertdatetime advlist lists checklist wordcount tinymcespellchecker a11ychecker textpattern noneditable help formatpainter pageembed charmap mentions quickbars linkchecker emoticons advtable'
  },
  menu: {
    tc: {
      title: 'TinyComments',
      items: 'addcomment showcomments deleteallconversations'
    }
  },
  menubar: 'file edit view insert format tools table tc help',
  toolbar: 'undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | a11ycheck ltr rtl | showcomments addcomment',
  autosave_ask_before_unload: true,
  autosave_interval: '30s',
  autosave_prefix: '{path}{query}-{id}-',
  autosave_restore_when_empty: false,
  autosave_retention: '2m',
  image_advtab: true,
          });
          
          
    }
})