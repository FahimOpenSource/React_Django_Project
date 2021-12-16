const useValidateUsername = (username, names) => {
  const invalid = /(?![@\.+\-_A-Za-z 0-9])./g.test(username);
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
