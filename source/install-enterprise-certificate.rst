Install enterprise certificate
*******************************

In order to use the client, the enterprise certificate must be set up according to your environment. We currently
support .NET Core, .NET Framework and Java.

.. NOTE::
   The .NET Framework version of the client only exists for versions 1 to 4. The documentation can be found `here <http://digipost.github.io/signature-api-client-dotnet/v4.x/>`_.


.NET Core
##########

The path and password to the certificate must be put somewhere safe. The path is:

.. tabs::

   .. tab:: Windows

      %APPDATA%\Microsoft\UserSecrets\<user_secrets_id>\secrets.json


   .. tab:: macOS

      ~/.microsoft/usersecrets/<user_secrets_id>/secrets.json

   .. tab:: Linux

      ~/.microsoft/usersecrets/<user_secrets_id>/secrets.json

.. TIP::
   For more information, please see the `Microsoft documentation <https://docs.microsoft.com/en-us/aspnet/core/security/app-secrets?view=aspnetcore-2.2&tabs=linux#how-the-secret-manager-tool-works>`_.


Add the following :code:`UserSecretsId` element to your :code:`.csproj` file:

.. code-block:: xml

   <PropertyGroup>
        <TargetFramework>netcoreapp2.1</TargetFramework>
        <UserSecretsId>organization-certificate</UserSecretsId>
   </PropertyGroup>

This means that the element :code:`<user_secrets_id>` in the path will be :code:`organization-certificate`.

From the command line, navigate to the directory where the current .csproj file is located and run the following commands with your own certificate values.

.. code-block:: bash

   dotnet user-secrets set "Certificate:Path:Absolute" "<your-certificate.p12>"
   dotnet user-secrets set "Certificate:Password" "<your-certificate-password>"







