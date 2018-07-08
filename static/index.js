function form () {
  var math = $('#math').val()
  var ipa = $('#ipa').val()
  var bing = $('#bing').val()
  var bind = $('#bind').val()
  var data = {bind, math, bing, ipa}
  return data
}

function callAPI () {
  var url = '/'
  var data = form()
  axios.post(url, data)
  .then(function(data) {
    $('.result').html(data.data)
  })
  .catch(function(err) {
    console.log(err);
  })
}

$('#submit').click(function() {
  callAPI()
})
