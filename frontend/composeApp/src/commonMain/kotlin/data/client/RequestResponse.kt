package data.client

import io.ktor.client.*
import io.ktor.client.plugins.contentnegotiation.*
import io.ktor.client.request.*
import io.ktor.client.statement.*
import io.ktor.http.*
import io.ktor.serialization.kotlinx.json.*


class RequestResponse {
    private val client = HttpClient {
        install(ContentNegotiation) {
            json()
        }
    }
    private val serverHost = "localhost"
    private val serverPort = 8080


    suspend fun getRequest(
        route: String,
        nameParameter: String? = null,
        valueParameter: String? = null,
    ): HttpResponse {
        val response: HttpResponse = client.get {
            url {
                host = serverHost
                port = serverPort
                path(route)
                if (nameParameter != null && valueParameter != null) {
                    parameters.append(nameParameter, valueParameter)
                }
            }
        }
        return response
    }


    suspend fun postRequest(route: String, data: Any): HttpResponse {
        val response: HttpResponse = client.post {
            url {
                host = serverHost
                port = serverPort
                path(route)
            }
            contentType(ContentType.Application.Json)
            setBody(data)
        }

        return response
    }


    suspend fun deleteRequest(route: String): HttpResponse {
        val response: HttpResponse = client.delete {
            url {
                host = serverHost
                port = serverPort
                path(route)
            }
        }

        return response
    }


    suspend fun putRequest(route: String, data: Any): HttpResponse {
        val response: HttpResponse = client.put {
            url {
                host = serverHost
                port = serverPort
                path(route)
            }
            contentType(ContentType.Application.Json)
            setBody(data)
        }

        return response
    }
}
