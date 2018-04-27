function handleSubmit() {
	
	var numQuestions = document.getElementsByClassName("questionDiv").length;
	var inputFields = document.getElementsByTagName("input");
	var checkedFields = 0;

	for(i = 0; i < inputFields.length; ++i){
		if (inputFields[i].checked){
			checkedFields++;
		}
	}
	if(checkedFields != numQuestions){
		alertify.error("You didn't completely fill out the form!");
		return false;
	}

	//pass it to the back end
}