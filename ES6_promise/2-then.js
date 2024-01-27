export default function handleResponseFromAPI(promise) {
  return promise
    /* eslint-disable */
    .then(() => { 
      return ({
        status: 200,
        body: 'success',
      });
    })
    /* eslint-enable */
    .catch(() => Error())
    .finally(() => {
      console.log('Got a response from the API');
    });
}
