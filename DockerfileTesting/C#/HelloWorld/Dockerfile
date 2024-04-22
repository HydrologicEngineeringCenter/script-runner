# https://stackoverflow.com/questions/70564222/how-to-compile-and-run-a-csharp-file-using-dockerfile
FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /app
RUN dotnet new console
COPY MyFile.cs Program.cs
RUN dotnet publish -c Release -o out

FROM mcr.microsoft.com/dotnet/runtime:6.0
WORKDIR /app
COPY --from=build /app/out .
ENTRYPOINT ["dotnet", "app.dll"]