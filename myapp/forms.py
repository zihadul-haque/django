from django import forms

class user_forms(forms.Form):

      #   <label for="user_name">Full Name</label>
      # <input type="text" name="user_name" placeholder="Enter your full name" value="" required>
      user_name=forms.CharField(label="Full Name",widget=forms.TextInput(attrs={"placeholder":'Enter your  full name',"style":'width:300px'}))
# widget=forms.TextInput(attrs={"placeholder":"Enter Your Full Name"})
      # <label for="user_email">User Email</label>
      # <input type="email" name="user_email" value="" required>
      user_dob=forms.DateField(label='Date of Birth',widget=forms.TextInput(attrs={"type":"date"}))
      user_email=forms.EmailField(label="User Email",widget=forms.TextInput(attrs={"placeholder":"Enter your email","style":'width:200px'}))
