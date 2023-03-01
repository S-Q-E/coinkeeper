<!-- The JavaScript code to handle the button clicks and show/hide the popup form -->

  const addTransactionBtn = document.querySelector('.add-transaction');
  const popupForm = document.querySelector('.popup-form');
  const closeBtn = document.createElement('button');

  // Set up the close button for the popup form
  closeBtn.innerText = 'Close';
  closeBtn.classList.add('btn');
  closeBtn.style.marginTop = '20px';
  closeBtn.addEventListener('click', () => {
    popupForm.style.display = 'none';
  });
  popupForm.appendChild(closeBtn);

  // Show the popup form when the "Add Transaction" button is clicked
  addTransactionBtn.addEventListener('click', () => {
    popupForm.style.display = 'block';
  });

  // Handle the form submission to add a new transaction
  const form = popupForm.querySelector('form');
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const title = form.querySelector('#title').value;
    const value = form.querySelector('#value').value;
    // Handle adding the new transaction to the list
    // ...
    // Hide the popup form
    popupForm.style.display = 'none';
  });
