package com.amazon.polly.demos.wordconverter.io;

import com.amazon.polly.demos.wordconverter.models.OutputContext;
import com.amazonaws.services.s3.model.ObjectMetadata;
import com.amazonaws.services.s3.model.ObjectTagging;
import com.amazonaws.services.s3.model.PutObjectRequest;
import com.amazonaws.services.s3.model.Tag;
import com.amazonaws.util.StringInputStream;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class S3OutputStrategy implements OutputStrategy {

    @Override
    public void saveFile(OutputContext outputContext) throws IOException {
        StringInputStream contentStream = new StringInputStream(outputContext.getContent());
        ObjectMetadata metadata = new ObjectMetadata();
        metadata.setContentLength(outputContext.getContent().getBytes().length);
		String fileNameUnsanitized = outputContext.getPrefix() + outputContext.getFileName() + ".txt";
		String fileNameSanitized = fileNameUnsanitized
									.replaceAll("[áàâä]", "a")
									.replaceAll("[éèêë]", "e")
									.replaceAll("[íìîï]", "i")
									.replaceAll("[óòôö]", "o")
									.replaceAll("[úùûü]", "u")
                                    .replaceAll("ñ", "n")
				    .replaceAll(":", "");

        PutObjectRequest putObjectRequest = new PutObjectRequest(
                outputContext.getBucketName(),
                fileNameSanitized,
                contentStream,
                metadata);

        List<Tag> tags = new ArrayList<>();
        tags.add(new Tag("VoiceId", outputContext.getVoiceId()));
        putObjectRequest.setTagging(new ObjectTagging(tags));

        outputContext.getS3Client().putObject(putObjectRequest);
    }
}
