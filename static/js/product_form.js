function readHeaderURL(input) {
    document.querySelector('.header-image-preview').innerHTML = '';
    if (input.files && input.files[0]) {
        var files = input.files

        for (let file of files) {
            if (file.size < 6000000) {
                let img = new Image;
                img.src = URL.createObjectURL(file);
                document.querySelector('.header-image-preview').appendChild(img);
            } else {
                alert('One or more of your files is too large, max 6MB');
            }
        }

    }
}

function readURL(input) {
    document.querySelector('.image-preview').innerHTML = '';
    if (input.files && input.files[0]) {
        var files = input.files

        for (let file of files) {
            if (file.size < 6000000) {
                let img = new Image;
                img.src = URL.createObjectURL(file);
                document.querySelector('.image-preview').appendChild(img);
            } else {
                alert('One or more of your files is too large, max 6MB');
            }
        }

    }
}

function displayFeatures() {
    $('.features').keyup(function () {
        $(this).next('.features').attr('hidden', false);
        if ($(this).find('.textInput').val() == '') {
            $(this).next('.features').attr('hidden', true);
        }
    });
}

function displayFacilities() {
    $('.facilities').keyup(function () {
        $(this).next('.facilities').attr('hidden', false);
        if ($(this).find('.textInput').val() == '') {
            $(this).next('.facilities').attr('hidden', true);
        }
    });
}

function setPriceDisabled() {
    if($('#id_poa')) {
        $('#id_poa').change(function () {
            if($(this).is(':checked')) {
                $('#id_price').attr('required', false);
                $('#div_id_price').attr('hidden', true);
                $('#or').attr('hidden', true);
                $('#id_price').val(0)
            } else {
                $('#id_price').attr('required', true);
                $('#div_id_price').attr('hidden', false);
                $('#or').attr('hidden', false);
            }
        });
    }
};

function removeIfLand() {
    if ($('#id_property_type')) {
        $('#id_property_type').change(function () {
            if ($(this).val().toLowerCase() == 'site' || $(this).val().toLowerCase() == 'land') {
                $('#id_no_of_bedrooms').attr('required', false);
                $('#id_no_of_bedrooms').val(0)
                $('#id_no_of_bathrooms').attr('required', false);
                $('#id_no_of_bathrooms').val(0)
                $('#id_no_of_single_bedrooms').attr('required', false);
                $('#id_no_of_single_bedrooms').val(0)
                $('#id_no_of_double_bedrooms').attr('required', false);
                $('#id_no_of_double_bedrooms').val(0)
                $('#id_no_of_twin_bedrooms').attr('required', false);
                $('#id_no_of_twin_bedrooms').val(0)
                $('#id_furnishing').attr('required', false);
                $('#id_furnishing').val('Unfurnished');
                $('#div_id_furnishing').attr('hidden', true);
                $('#bedBathInputs').attr('hidden', true);
                $('#rentBedsInputs').attr('hidden', true);
                $('#rentBathroomsInput').attr('hidden', true);
            } else {
                $('#id_no_of_bedrooms').attr('required', true);
                $('#id_no_of_bathrooms').attr('required', true);
                $('#id_no_of_single_bedrooms').attr('required', true);
                $('#id_no_of_double_bedrooms').attr('required', true);
                $('#id_no_of_twin_bedrooms').attr('required', true);
                $('#id_furnishing').attr('required', true);
                $('#div_id_furnishing').attr('hidden', false);
                $('#bedBathInputs').attr('hidden', false);
                $('#rentBedsInputs').attr('hidden', false);
                $('#rentBathroomsInput').attr('hidden', false);
            }
        });
    }
};

removeIfLand();
displayFacilities();
displayFeatures();
setPriceDisabled();