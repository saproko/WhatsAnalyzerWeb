/* ---index page file upload--- */

function is_file_uploaded() {
  var files = document.getElementById("file-upload-button").files;
  return files.length > 0;
}

function submit_button_click() {
  if (is_file_uploaded()) {
    loading();
    document.getElementById("submit-button").click();
  } else {
    alert("Bitte lade zuerst deine Chatdatei hoch.");
  }
}

function file_upload_button_click() {
  document.getElementById("file-upload-button").click();
}

$("#file-upload-card").change(function () {
  var submit_card = document.getElementById("submit-card");

  if (is_file_uploaded()) {
    submit_card.style.background = "rgb(2, 117, 216)";
    submit_card.style.color = "white";
  } else {
    submit_card.style.background = "rgb(236, 239, 244)";
    submit_card.style.color = "rgb(110, 117, 125)";
  }
});

function loading() {
  $("#loading").show();
  $("#content").hide();
}
