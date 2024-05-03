$(document).ready(function () {
  $('#add_items').click(function () {
    $("<li>").text("Item").appendTo("ul.my_list");
  });
  $('#remove_item').click(function () {
    $('ul.my_list li:last-child').remove();
  });
  $('#clear_list').click(function () {
    $("ul.my_list").empty();
  });
});
