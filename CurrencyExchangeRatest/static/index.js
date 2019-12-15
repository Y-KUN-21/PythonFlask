document.addEventListener('DOMContentLoaded',()=>
{
		
		document.querySelectorAll('#form').onsubmit=()=>

		{

			const request= new XMLHttpRequest;
			const Currency=document.querySelector('#Currency').value;
			request('POST','/xrates/');


			request.onload=()=>
			{

				const data =JSON.parse(request.responseText);
            
	            if (data.success) 
	            {
	                const contents = "1 USD is equal to "+ ${data.rate}+${Currency}.
	                document.querySelector('#ExRates').innerHTML = contents;
	            }
	            else 
	            {
	                document.querySelector('#ExRates').innerHTML = 'There was an error.';
	            }

		    }

	        const data = new FormData();
	        data.append('Currency', Currency);

	        // Send request
	        request.send(data);
	        return false;
     	};
		
	});
