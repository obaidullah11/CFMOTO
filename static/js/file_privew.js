// Assuming this code is inside a function or script
document.addEventListener('DOMContentLoaded', function () {
    // Find the file input element
    var input = document.getElementById('your-file-input-id'); // Replace with the actual ID

    // Function to create a preview of the selected image
    function createPreview(imageUrl) {
        var preview = document.createElement('img');
        preview.src = imageUrl;
        preview.classList.add('preview-image');

        // Insert the preview after the file input
        input.insertAdjacentElement('afterend', preview);
        console.log('Image inserted after file input:', preview);
    }

    // Event listener for file selection
    input.addEventListener('change', function () {
        console.log('File input changed:', this.files);

        if (this.files && this.files[0]) {
            var reader = new FileReader();

            // FileReader onload callback
            reader.onload = function (e) {
                console.log('FileReader loaded:', e);
                createPreview(e.target.result);
            };

            // FileReader onerror callback
            reader.onerror = function (e) {
                console.error('FileReader error:', e);
            };

            reader.readAsDataURL(this.files[0]);
        }
    });

    // Check for an existing image on page load (for edit view)
    var currentImage = input.getAttribute('data-initial-file');
    if (currentImage) {
        console.log('Initial image found:', currentImage);
        createPreview(currentImage);
    }
    
    // Example: Checking for change permission and displaying a preview
    var hasChangePermission = true; // Replace with your logic to check change permission
    if (hasChangePermission) {
        var editImage = input.getAttribute('data-edit-file');
        if (editImage) {
            console.log('Edit image found:', editImage);
            createPreview(editImage);
        }
    }
});

