# Fix xampp shutdown unexpectedly

![xamp_error](https://user-images.githubusercontent.com/83243886/197918171-c8ef9c8b-a53c-4550-9abc-fa5cb227d082.jpg)

This error can occur because another application is using the port that xampp uses. It can also be because 
“missing dependencies, improper privileges, a crash, or a shutdown by another method.”

Anyway, I found the solution in this interesting article https://kinsta.com/knowledgebase/xampp-error-apache-shutdown-unexpectedly/#:~:text=The%20XAMPP%20error%20%E2%80%9CApache%20shutdown%20unexpectedly%E2%80%9D%20is%20commonly%20caused%20by,update%20XAMPP's%20Apache%20configuration%20settings. <br/>
It's easy to do but it becomes tedious to repeat it, so I decided to automate it
