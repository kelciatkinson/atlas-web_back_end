import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((results) => {
      const filteredResults = results.filter((result) => result.status === 'fulfilled');
      return filteredResults.map((result) => result.value);
    });
}
