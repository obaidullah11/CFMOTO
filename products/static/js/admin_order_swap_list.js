$(document).ready(function() {
    // Find the list items in the admin list view
    var listItems = $('tbody tr');

    // Handle the "dblclick" event to swap list items
    listItems.on('dblclick', function() {
        var selectedListItems = listItems.filter('.selected');

        if (selectedListItems.length === 2) {
            var firstItem = selectedListItems.first();
            var secondItem = selectedListItems.last();
            var temp = firstItem.html();
            firstItem.html(secondItem.html());
            secondItem.html(temp);
        }
    });
});
