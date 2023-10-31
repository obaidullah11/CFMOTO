$(document).ready(function() {
    console.log("script loaddedd 1")
    $('#id_series').change(function() {
        var categoryId = $(this).val();
        $.ajax({
            url: '/vehicles/get_attributes/',
            data: {'category_id': categoryId},
            success: function(data) {
                console.log("data-----------------> ", data)
                var modelOptions = data?.Factory_name.map(function(item) {
                    return '<option value="' + item.id + '">' + item.name + '</option>';
                }).join('');
                $('#id_Factory_name').html('<option value="">---------</option>' + modelOptions);

                var modelOptions = data?.ModelName.map(function(item) {
                    return '<option value="' + item.id + '">' + item.name + '</option>';
                }).join('');
                $('#id_model_name').html('<option value="">---------</option>' + modelOptions);

                var wheelOptions = data?.EUTypeApproval.map(function(item) {
                    return '<option value="' + item.id + '">' + item.name + '</option>';
                }).join('');
                $('#id_eu_type').html('<option value="">---------</option>' + wheelOptions);

                var screenOptions = data?.SteeringPower.map(function(item) {
                    return '<option value="' + item.id + '">' + item.name + '</option>';
                }).join('');
                $('#id_steering_power').html('<option value="">---------</option>' + screenOptions);

                var registrationOptions = data?.Wheels.map(function(item) {
                    return '<option value="' + item.id + '">' + item.name + '</option>';
                }).join('');
                $('#id_wheels').html('<option value="">---------</option>' + registrationOptions);



                var registrationOptions = data?.Color.map(function(item) {
                    return '<option value="' + item.id + '">' + item.name + '</option>';
                }).join('');
                $('#id_color').html('<option value="">---------</option>' + registrationOptions);

                var registrationOptions = data?.Screen.map(function(item) {
                    return '<option value="' + item.id + '">' + item.name + '</option>';
                }).join('');
                $('#id_screen').html('<option value="">---------</option>' + registrationOptions);

                var registrationOptions = data?.CargoCompartment.map(function(item) {
                    return '<option value="' + item.id + '">' + item.name + '</option>';
                }).join('');
                $('#id_cargo_compartment').html('<option value="">---------</option>' + registrationOptions);

                var registrationOptions = data?.CommunicationTerminal.map(function(item) {
                    return '<option value="' + item.id + '">' + item.name + '</option>';
                }).join('');
                $('#id_communication_terminal').html('<option value="">---------</option>' + registrationOptions);

                var registrationOptions = data?.SKU.map(function(item) {
                    return '<option value="' + item.id + '">' + item.name + '</option>';
                }).join('');
                $('#id_sku').html('<option value="">---------</option>' + registrationOptions);
            }
        });
    });
});
