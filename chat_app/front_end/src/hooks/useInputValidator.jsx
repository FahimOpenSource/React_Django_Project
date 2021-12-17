const useInputValidator = (field, field_value, valid) => {

  Object.keys(valid).forEach((key) => {
    if (key === field.id) {
      console.log(valid[key]);
      if (valid[key] === false) {
        field.classList.add("ring-2", "ring-red-450");
      } else {
        field.classList.remove("ring-2", "ring-red-450");
      }
    }
  }, console.log(valid));

  if (field.value === "" || field.value === " ") {
    field.nextSibling.innerHTML = "*Required";
    field.nextSibling.classList.add("text-red-450");
    console.log("herrerr",valid)
  } else {
    field.nextSibling.classList.remove("text-red-450");
    field.nextSibling.innerHTML = "";
  }

  const input = field.value;
  const last_input_char = input.charAt(input.length - 1);

  if (last_input_char === " ") {
    if (field_value !== "") {
      const last_init_char = field_value.charAt(field_value.length - 1);
      if (last_init_char == " ") {
        return false;
      } else {
        return true;
      }
    }
  } else {
    return true;
  }
};

export default useInputValidator;
