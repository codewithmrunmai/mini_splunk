package com.splunk.gateway;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.gateway.route.RouteLocator;
import org.springframework.cloud.gateway.route.builder.RouteLocatorBuilder;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class ApiGatewayApplication {

    public static void main(String[] args) {
        SpringApplication.run(ApiGatewayApplication.class, args);
    }

    @Bean
    public RouteLocator customRouteLocator(RouteLocatorBuilder builder) {
        return builder.routes()
            // Auth Service routes
            .route("auth-service", r -> r.path("/api/auth/**")
                .uri("http://auth-service:8081"))

            // Event Service routes
            .route("event-service", r -> r.path("/api/events/**")
                .uri("http://event-service:8082"))

            // Detection Service routes
            .route("detection-service", r -> r.path("/api/incidents/**")
                .uri("http://detection-service:8083"))

            .build();
    }
}
