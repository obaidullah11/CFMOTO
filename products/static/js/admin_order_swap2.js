(function ($) {
    // Log a message when the document is fully loaded
    $(document).ready(function () {
        console.log('Document is fully loaded.');

        // Find the select element with the specified ID
        var selectBox = $('select#id_Maintenance_List_Point_name');

        // // Enable drag-and-drop for the select box options
        // selectBox.sortable({
        //     axis: 'y', // Enable vertical sorting
        //     items: 'option', // Sort only the option elements
        // });

        // Log a message when options are reordered and update the order field
        selectBox.on('sortupdate', function (event, ui) {
            console.log('Options reordered.');

            // Get all the option elements in the select box
            var options = selectBox.find('option');

            // Iterate through the options and update the order in the database
            options.each(function (index) {
                var optionValue = $(this).val();
                // Send an AJAX request to update the order in the database
                $.ajax({
                    url: '/update_order/', // Replace with your URL for updating the order
                    method: 'POST',
                    data: {
                        option_id: optionValue,
                        new_order: index,
                    },
                    success: function (response) {
                        // Handle the response if needed
                    },
                });
            });
        });
    });
})(django.jQuery);

