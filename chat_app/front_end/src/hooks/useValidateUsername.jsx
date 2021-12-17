const useValidateUsername = (username, names) => {
  
  let taken = false;
  if (username !== "") {
    for (var name of names.list) {
      if (name.includes(username)) {
        taken = true;
      }
    }
  }

  return {
    taken,
    invalid,
  };
};

export default useValidateUsername;
