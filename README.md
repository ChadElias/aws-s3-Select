# Project Title

AWS S3 Select Lambda in Python

## Information

Login to the AWS Console.

```
Create a new IAM Role and paste the PolicyForLambda.json as an in-line policy for the role.
```

```
Create a new Empty Lambda Function with Python 3.6 as the RunTime
```

```
Select Edit Code Inline and paste the contents of s3Select.py into the Cloud 9 Editor
```

```
Scroll down to the section called "Environment Variables"
```

```
Add a Key named 'BUCKET_NAME' and its Value should be the bucket that you want to get the JSON data from
```

## Authors

* **Chad Elias**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details