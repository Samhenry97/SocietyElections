function handleSubmit() {
  		//get the number of questions
	    var numQuestions = document.getElementsByClassName("questionDiv").length;

	    //get the number of input fields
		var inputFields = document.getElementsByTagName("input");
		var checkedFields = 0;

		//for every input field that is checked, increment the checked fields variable
		for(i = 0; i < inputFields.length; ++i){
			//since the input fields are radio buttons, only one will be checked at a time.
			if (inputFields[i].checked){
				checkedFields++;
			}
		}
		if(checkedFields != numQuestions){
			alertify.error("You didn't completely fill out the form!");
			return false;
		} else {
			 return true;
		}
			
}