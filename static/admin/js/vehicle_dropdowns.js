window.addEventListener('DOMContentLoaded', (event) => {
    const categorySelect = document.getElementById('id_CATEGORY');
    const modelSkuSelect = document.getElementById('id_MODEL_SKU');
    const modelNameSelect = document.getElementById('id_MODEL_NAME');

    // Disable the dependent dropdowns initially
    modelSkuSelect.disabled = true;
    modelNameSelect.disabled = true;

    // Event listener for the categorySelect change event
    categorySelect.addEventListener('change', function() {
        // Disable dependent dropdowns if no option is selected
        if (categorySelect.value === '') {
            modelSkuSelect.disabled = true;
            modelNameSelect.disabled = true;
            return;
        }

        // Fetch the options for the modelSkuSelect dropdown based on the selected category
        fetch(`/api/get_model_skus/?category=${categorySelect.value}`)
            .then(response => response.json())
            .then(data => {
                // Populate the modelSkuSelect dropdown with the fetched options
                modelSkuSelect.innerHTML = '';
                modelSkuSelect.disabled = false;
                modelNameSelect.disabled = true;

                const defaultOption = document.createElement('option');
                defaultOption.text = '---------';
                modelSkuSelect.appendChild(defaultOption);

                for (let option of data) {
                    const newOption = document.createElement('option');
                    newOption.value = option.model_sku;
                    newOption.text = option.model_sku;
                    modelSkuSelect.appendChild(newOption);
                }
            });
    });

    // Event listener for the modelSkuSelect change event
    modelSkuSelect.addEventListener('change', function() {
        // Disable dependent dropdown if no option is selected
        if (modelSkuSelect.value === '') {
            modelNameSelect.disabled = true;
            return;
        }

        // Fetch the options for the modelNameSelect dropdown based on the selected model SKU
        fetch(`/api/get_model_names/?model_sku=${modelSkuSelect.value}`)
            .then(response => response.json())
            .then(data => {
                // Populate the modelNameSelect dropdown with the fetched options
                modelNameSelect.innerHTML = '';
                modelNameSelect.disabled = false;

                const defaultOption = document.createElement('option');
                defaultOption.text = '---------';
                modelNameSelect.appendChild(defaultOption);

                for (let option of data) {
                    const newOption = document.createElement('option');
                    newOption.value = option.model_name;
                    newOption.text = option.model_name;
                    modelNameSelect.appendChild(newOption);
                }
            });
    });
});
