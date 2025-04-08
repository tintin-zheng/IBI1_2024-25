"""
pseudocode:
define a function drug_dosage_calculator with parameters weight and strength
    check if strength is correct (either "120 mg/5 ml" or "250 mg/5 ml")
        check if weight is in the range of 10 kg to 100 kg
            calculate total drug weight based on strength
                
"""



# Drug Dosage Calculator
def drug_dosage_calculator(weight, strength):
    """
    Input:
        weight: weight of the patient in kg
        strength: strength of the drug in mg/ml (e.g., "120 mg/5 ml" or "250 mg/5 ml")
    Returns the volume of drug to be administered in ml
    """
    # Check if the strength is correct
    if strength == "120 mg/5 ml" or strength == "250 mg/5 ml":
        # Check if the weight is in the range of 10 kg to 100 kg
        if 10 <= weight <= 100 :
            # Calculate the total drug weight based on the strength
            total_drug_weight = weight*15
            # judge the strength
            if strength == "120 mg/5 ml":
                # Calculate the total drug volume based on the strength
                total_drug_volume = (total_drug_weight/120)*5
                return f"Your drug volume is {total_drug_volume} ml"
            else :
                total_drug_volume = (total_drug_weight/250)*5
                return f"Your drug volume is {total_drug_volume} ml"


        else:
            return "Your weight is out of range(10 kg to 100 kg)"
    else:
        return "Place enter the correct strength.(120 mg/5 ml or 250 mg/5 ml)"



# Example usage:
# weight = 50 kg
# strength = "120 mg/5 ml"
print(drug_dosage_calculator(50, "120 mg/5 ml"))
# Output: Your drug volume is 3.125 ml 
    



